var start = "A1";
var end = "A1";
$(document).ready(function() {
    var squares = document.getElementsByClassName("square");
    for(var i = 0; i < squares.length; i++) {
        var count = i;
        squares[count].addEventListener("click", initStart);
        /*if(squares[i].innerHTML == "") {
            continue;
        }*/
        // add click event for each piece
        // alert("#" + squares[i].id + " span");
       /*var innerSpans = squares[count].getElementsByTagName("SPAN");
        if(innerSpans[0] != undefined) {
            var innerClasses = innerSpans[0].className;
            squares[count].addEventListener("click", function() {
                movement(squares[count].id, innerClasses);
            });
        }*/
        // alert("#" + squares[i].id + " span");
    }
});

function convertToStart() {
    var squares = document.getElementsByClassName("square");
    for(var i = 0; i < squares.length; i++) {
        var count = i;
        squares[count].removeEventListener("click", initEnd);
        squares[count].addEventListener("click", initStart);
    }
}

function initStart() {
    start = this.id;
    convertToEnd();
}

function convertToEnd() {
    var squares = document.getElementsByClassName("square");
    for(var i = 0; i < squares.length; i++) {
        var count = i;
        squares[count].removeEventListener("click", initStart);
        squares[count].addEventListener("click", initEnd);
    }
}

function initEnd() {
    end = this.id;
    postMovement(start, end);
}

function movement(id, classes) {
    // determine movement spaces based on piece classes
    var yAxis = "ABCDEFGH";
    var direction = 1;
    var xCoOrd = id[1];
    var xMax = 0;
    var yCoOrd = yAxis.indexOf(id[0]);
    var yMax = 0;
    var movementSpace;
    var i;
    var left;
    var right;
    var up;
    var down;
    var curSpace;
    if(classes.indexOf("pawn") > -1) {
        direction = classes.indexOf("white") > -1 ? -1 : 1;
        yMax = yCoOrd == 1 || yCoOrd == 6 ? 2 : 1;
        for(i = 0; i < yMax; i++) {
            curSpace = yAxis[yCoOrd + (i * direction)] + xCoOrd;
            movementSpace = document.getElementById(curSpace);
            if(movementSpace.innerHTML == "") {
                movementSpace.className += "move-space";
                movementSpace.addEventListener("click", function() {
                    postMovement(id, movementSpace.id);
                });
            }
        }
    } else if(classes.indexOf("rook") > -1) {
        for(left = xCoOrd; left > 0; left--) {
            curSpace = yAxis[yCoOrd] + left;
            movementSpace = $("#" + curSpace);
            if(movementSpace.innerHTML == "") {
                break;
            }
            movementSpace.className += "move-space";
            movementSpace.addEventListener("click", function() { postMovement(id, movementSpace.id); });
            movementSpace.removeEventListener("click", function() { postMovement(id, movementSpace.id); });
        }
    }
}

// post plays to backend, then change board based on response
function postMovement(start, end) {
    document.getElementById("error").innerHTML = "";
    var turn = document.getElementById("turn");
    var colour = turn.innerHTML == "Blue's Turn" ? "W" : "B";
    var superpos = sp.checked ? "True" : "False";
    $.post("/home", { "sp" : superpos, "colour" : colour, "start" : start, "end" : end }, function(data) {
        result = data.split(",");
        if(result[0] == "success") { // if backend function returns true
            if(result[1] == "success") {
                findAndDestroy(document.getElementById(end).getElementsByClassName("piece")[0].id);
            }
            makeMove(start, end);
        } else {
            document.getElementById("error").innerHTML = "Your move was invalid";
        }
    });
    convertToStart();
}

function findAndDestroy(tag) {
    tag = tag.substring(0, tag.length - 1);
    var pieces = document.getElementsByClassName("piece");
    for(var i = 0; i < pieces.length; i++) {
        if(pieces[i].id.indexOf(tag) > -1) {
            pieces[i].innerHTML = "";
        }
    }
}

function makeMove(start, end) {
    var startSquare = document.getElementById(start);
    var endSquare = document.getElementById(end);
    endSquare.innerHTML = startSquare.innerHTML;
    if(!sp.checked) {
        startSquare.innerHTML = "";
    } else {
        var endPiece = endSquare.getElementsByClassName("piece")[0];
        endPiece.id += "1";
    }
    if(turn.innerHTML == "Blue's Turn") {
        turn.innerHTML = "Red's Turn";
        turn.className = "pc-black text-center";
    } else {
        turn.innerHTML = "Blue's Turn";
        turn.className = "pc-white text-center";
    }
}