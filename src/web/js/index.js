var index = {
    LayerControl: {
        leftVisible: false,
        rightVisible: false,

        onMouseWheellLeft: function(){
            console.log("left");
            if (index.LayerControl.leftVisible) {
                index.LayerControl.hideLeftLayer();
            }
            else {
                index.LayerControl.showRightLayer();
            }
        },

        onMouseWheellRight: function(){
            console.log("right");
            if (index.LayerControl.rightVisible){
                index.LayerControl.hideRightLayer();
            }
            else {
                index.LayerControl.showLeftLayer();
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
                index.LayerControl.onMouseWheellLeft();
            } 
            if (event.deltaX < 0) {
                index.LayerControl.onMouseWheellRight();
            }
            if (event.deltaY < 0) {
                index.LayerControl.onMouseWheellUp();
            }
            if (event.deltaY > 0) {
                index.LayerControl.onMouseWheellDown();
            }
        },

        showLeftLayer: function(event){
            $(".left-layer").width("36%");
            index.LayerControl.leftVisible = true;
        },

        hideLeftLayer: function(event){
            $(".left-layer").width("0px");
            index.LayerControl.leftVisible= false;
        },

        showRightLayer: function(event){
            $(".right-layer").width("36%");
            index.LayerControl.rightVisible = true;
        },

        hideRightLayer: function(event){
            $(".right-layer").width("0px");
            index.LayerControl.rightVisible = false;
        }
    }
};

$(function(){
    console.log("Index Js Runing ~");

    $(document).on('mousewheel', _.debounce(index.LayerControl.onMouseWheel, 100, true));

    $(document).bind('keydown', 'ctrl+f', function(e){
        $('#search').focus();
    });

    $(document).bind('keydown', 'ctrl+r', function(e){
        location.reload();
    });

    $(window).resize(function(){
        var search_height = $(".search_container").outerHeight(true);
        var split_line = $(".music-table-container").outerHeight(true) * 2;
        var control_height = $(".player-control-container").outerHeight(true);
        var window_height = $(window).height();

        $("songs-container").height(window_height-search_height-
                split_line-control_height-30);
    });

});
