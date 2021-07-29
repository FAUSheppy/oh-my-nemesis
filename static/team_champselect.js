function saveToServer(){
    var xhttp = new XMLHttpRequest();
	
	champ = "Atrox"
	position = "Top"
	affinity = "5"
	
	req = "/save?type=teamChampSelect" 	+ "&champ=" + cahmp
										+ "&position=" + position
										+ "&affinity=" + affinity
	xhttp.open("POST", req, true);
    //xhttp.setRequestHeader('Content-Type', 'application/json');
    xhttp.send(json)
}

	
function addChamp(selectorId, role){
	champ = document.getElementById(selectorId).value
	url   = window.location.href + "?" + "role="   + role  +
								   "&" + "champ="  + champ +
								   "&" + "action=" + "add"
	fetch(url, {
		method: 'POST',
		mode: 'cors',
		credentials: 'same-origin',
		headers: {
			'Content-Type': 'application/x-www-form-urlencoded',
		},
		referrerPolicy: 'strict-origin'
		}
	).then(window.location.reload());
}


function removeChamp(champ, role){		
	url   = window.location.href + "?" + "role="  + role   +
								   "&" + "champ=" + champ  +
								   "&" + "action=" + "remove"
	fetch(url, {
		method: 'POST',
		mode: 'cors',
		credentials: 'same-origin',
		headers: {
			'Content-Type': 'application/x-www-form-urlencoded',
		},
		referrerPolicy: 'strict-origin'
		}
	).then(window.location.reload());
}