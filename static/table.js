var currentCellSelected = null


var colors = ["rgb(245, 247, 246)", "indianred", "coral", "orange", "yellow", "cyan", "lightgreen", "rgb(75, 140, 72)", "rgb(35, 110, 31)"]
var words  = ["", "Awefull", "Worse", "Bad", "Normal", "Praticed", "Decent", "Good", "Perfect"]


function cellOnClickListener(element){
    updateSelectedCell(element)
}

function colorCellOnClickListener(element){
    if(currentCellSelected){
        currentCellSelected.style.background = element.style.background
    }
}

function updateSelectedCell(cell){
    if(currentCellSelected && currentCellSelected.id != cell.id){
        currentCellSelected.style.borderColor = ""
        currentCellSelected.blur()
    }
    currentCellSelected = cell
    if(cell){
        cell.style.borderColor = "blue"
    }
}

function updateBackgroundForCell(cell, indexMod){
    if(!cell.style.background){
        cell.style.background = colors[0];
    }

    /* firefox hack */
    var bcolor = cell.style.background
    if(bcolor.indexOf(") ")>0){
        bcolor = bcolor.split(") ")[0] + ")"
    }else if(bcolor.indexOf(" ") && bcolor.indexOf("rgb") == -1){
        bcolor = bcolor.split(" ")[0]
    }

    console.log(bcolor)
    newColor = colors.indexOf(bcolor) + indexMod + colors.length
    cell.style.background = colors[newColor % colors.length]
}

function addWindowListeners(){
    var colorContent = ""
    var i
    for(i = 1; i < colors.length; i++){
        var colorCell = '<td class="cell color-cell" onclick="colorCellOnClickListener(this)" '
                    + 'style="border-style: none; background: ' 
                    + colors[i] + '">' + words[i] + '</td>\n'
        colorContent += colorCell 
    }
    document.getElementById("colorExplanation").innerHTML = colorContent

    document.body.addEventListener('keyup', (e) => {
        if(!currentCellSelected){
            updateSelectedCell(document.getElementById("0"))
        }

        var cols = document.getElementById('table').rows[0].cells.length
        var rows  = document.getElementById('table').rows.length
        var id = parseInt(currentCellSelected.id)

        if(e.code === "ArrowUp" && document.activeElement == document.body){
            var targetId = Math.max(id-cols, 0)
            updateSelectedCell(document.getElementById(targetId))
            e.preventDefault()
        }else if(e.code === "ArrowDown" && document.activeElement == document.body){
            var targetId = Math.min(id+cols, cols*rows)
            updateSelectedCell(document.getElementById(targetId))
            e.preventDefault()
        }else if(e.code === "ArrowLeft" && document.activeElement == document.body){
            var targetId = Math.max(id-1, 0)
            updateSelectedCell(document.getElementById(targetId))
            e.preventDefault()
        }else if(e.code === "ArrowRight" && document.activeElement == document.body){
            var targetId = Math.min(id+1, cols*rows)
            updateSelectedCell(document.getElementById(targetId))
            e.preventDefault()
        }else if(e.code === "Escape"){
            updateSelectedCell(null)
            e.preventDefault()
        }else if(e.code === "ShiftLeft"){
            updateBackgroundForCell(currentCellSelected, +1)
            e.preventDefault()
        }else if(e.code === "ControlLeft"){
            updateBackgroundForCell(currentCellSelected, -1)
            e.preventDefault()
        }else if(e.code === "Enter"){
            if(document.activeElement != document.body){
                // document.activeElement.blur()
            }else{
                if(currentCellSelected){
                    currentCellSelected.focus()
                }
            }
            e.preventDefault()
        }else if(e.code === "Tab"){
            if(document.activeElement != document.body){
                document.activeElement.blur()
            }

            if(currentCellSelected){
                var targetId = Math.min(id+1, cols*rows)
                updateSelectedCell(document.getElementById(targetId))
            }
            e.preventDefault()
        }
    });
}

function saveToServer(){
    var contents = []
    var colors   = []

    for(let el of document.getElementsByClassName("cell")){
        if(!el.id){
            /* filter color cells */
            continue
        }
        contents = contents.concat(el.innerText)
        colors = colors.concat(el.style.background)
    }

    var cols = document.getElementById('table').rows[0].cells.length
    var rows = document.getElementById('table').rows.length
    var hasHeaderColumn = document.getElementById("hasHeaderColumn").innerText
    var hasHeaderRow    = document.getElementById("hasHeaderRow").innerText
    var dict = { contents:contents, colors:colors, rows:rows, cols:cols,
                 hasHeaderRow:hasHeaderRow, hasHeaderColumn:hasHeaderColumn };
    var json = JSON.stringify(dict);

    var tableId = document.getElementById("tableId").innerText

    var xhttp = new XMLHttpRequest();
    xhttp.onload = function() {
        if (xhttp.status != 204) {
            alert("Transmission failed!?!")
        }else{
            window.location.href = "/table?id=" + tableId
        }
    }

    xhttp.open("POST", "/save?id=" + tableId, true);
    xhttp.setRequestHeader('Content-Type', 'application/json');
    xhttp.send(json)
}

window.onload = addWindowListeners
