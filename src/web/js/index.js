var index = {

    leftVisible: false,
    rightVisible: false,

    onMouseWheellLeft: function(){
        console.log("left");
        if (index.leftVisible) {
            $(".left-layer").width("0px");
            index.leftVisible= false;
        }
        else {
            $(".right-layer").width("36%");
            index.rightVisible = true;
        }
    },

    onMouseWheellRight: function(){
        console.log("right");
        if (index.rightVisible){
            $(".right-layer").width("0px");
            index.rightVisible = false;
        }
        else {
            $(".left-layer").width("36%");
            index.leftVisible = true;
        }
    },

    onMouseWheellDown: function(){
        console.log("down");
    },

    onMouseWheellUp: function(){
        console.log("up");
    },

    onMouseWheel: function(event){
        // console.log(event.deltaX, event.deltaY, event.deltaFactor);
        if (event.deltaX > 0) {
            index.onMouseWheellLeft();
        } 
        if (event.deltaX < 0) {
            index.onMouseWheellRight();
        }
        if (event.deltaY < 0) {
            index.onMouseWheellUp();
        }
        if (event.deltaY > 0) {
            index.onMouseWheellDown();
        }
    }
}

$(function(){
    console.log("Index Js Runing ~");

    $(document).on('mousewheel', _.debounce(index.onMouseWheel, 60, true));
});
