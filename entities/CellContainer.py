import flask
class CellContainer:

    def __init__(self, tableConfig):

        self.columns       = tableConfig.get("columns")
        self.rows          = tableConfig["rows"]
        self.headerRow     = tableConfig["header-row"]
        if not self.columns:
            self.columns = len(self.headerRow)
        self.headerColumn  = tableConfig["header-column"]
        self.currentCellId = 0
        self.contents      = tableConfig.get("contents")
        self.colors        = tableConfig.get("colors")
        self.help          = tableConfig.get("help")

        self.hasHeaderColumn = bool(tableConfig.get("hasHeaderColumn"))
        self.hasHeaderRow    = bool(tableConfig.get("hasHeaderRow"))
    
    def setContents(self, contents):
        self.contents = contents

    def getView(self):
        innerHTML = ""
        startAtRow = 0
        if self.headerRow or self.hasHeaderRow:
            innerHTML += flask.Markup(flask.render_template("entities/row.html", cells=self.getHeaderRow()))
            startAtRow = 1
        for rowNr in range(startAtRow, self.rows):
            innerHTML += flask.Markup(flask.render_template("entities/row.html", cells=self.getRowHTML(rowNr)))
        return flask.Markup(flask.render_template("entities/table.html", tableContent=innerHTML))

    def getHeaderRow(self):
        rowHTML = ""
        array = None
        if self.contents:
            array = self.contents[:self.columns]
        else:
            array = self.headerRow
        for rowStr in array:
            rowHTML += flask.Markup(flask.render_template("entities/cell.html",
                                    cellId=self.currentCellId, classes="cell header", cellContent=rowStr))
            self.currentCellId += 1
        return rowHTML

    def getCellWidth(self):
        return "{:.2f}%".format(100/self.columns)

    def getRowHTML(self, curRow):
        '''Get HTML for individual rows'''

        rowHTML = ""
        for col in range(0, self.columns):

            # handle header fields in rows #
            classes = ["cell"]
            cellContent = ""
            cellColor   = ""
            if self.headerColumn and col == 0:
                classes += ["header"]
                cellContent = self.headerColumn[curRow]
            elif self.hasHeaderColumn and col == 0:
                classes += ["header"]
            if self.contents:
                cellContent = self.contents[curRow*self.columns+col]
            if self.colors:
                cellColor = self.colors[curRow*self.columns+col]

            # add single cell #
            rowHTML += flask.Markup(flask.render_template("entities/cell.html", cellId=self.currentCellId, cellContent=cellContent, classes=" ".join(classes), enableEdit=True, cellColor=cellColor))
            self.currentCellId += 1

        # return HTML for row #
        return rowHTML
