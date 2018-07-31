var Piece = {
    id : "",
    color : "",
    firstSuperPos : true,
    superPosNum : 0,
    superPosition : function() {
        if(this.firstSuperPos) {
            this.firstSuperPos = false;
        }
    },
    // attack : attack(),
};
$(document).ready(function() {
    var canvas  = document.getElementById("qccanvas");
    var ctx = canvas.getContext("2d");
    for(var i = 0; i < 300; i += 20) {
        ctx.fillRect(i, i, i + 40, i + );
    }
    ctx.fillRect(0, 0, 280, 138);
});