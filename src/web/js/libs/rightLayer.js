var rightLayer = {

    currentActivePlaylistEle: null,
    
    loadUserPlaylists: function(playlists){
        var pMineEle = $("#mine-playlists-container");
        var pCollectionEle = $("#collection-playlists-container");
        var uid = python.get_user_id();
        for (var i=0; i<playlists.length; i++){
            var ele = $("<div class='playlist-title no-selection btn'/>");
            var pid = playlists[i].id;
            ele.attr('pid', pid);
            if (playlists[i].uid === uid){
                if (playlists[i].type == 5) {
                    ele.text("◉ "+playlists[i].name);
                    rightLayer.activePlaylistEle(ele);
                    try {
                        content.loadPlaylist(parseInt(pid));
                    } catch (e){
                        console.error(e);
                        console.error("Load Playlist error");
                    }
                } else {
                    ele.text("◈ "+playlists[i].name);
                }
                pMineEle.append(ele);
            } else {
                pCollectionEle.append(ele);
                ele.text("◈ "+playlists[i].name);
            }
        }
        rightLayer.bindClickTrigger();
    },

    activePlaylistEle: function(ele){
        if (rightLayer.currentActivePlaylistEle !== null){
            rightLayer.currentActivePlaylistEle.removeClass('active');
        }
        ele.addClass('active');
    },

    bindClickTrigger: function(){
        $(".playlist-title").click(function(){
            var pid = parseInt($(this).attr('pid'));
            rightLayer.activePlaylistEle($(this));
            content.loadPlaylist(pid);
        });
    },

    ok: function(){
        console.log("rightLayer Ok");
    }
};


$(function(){
    rightLayer.bindClickTrigger();
});
