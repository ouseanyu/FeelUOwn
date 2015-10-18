var content = {
    loadPlaylist: function(pid, useCache){
        useCache = typeof useCache !== 'undefined' ? useCache : true;
        var data = python.get_playlist(pid, useCache);
        if (data !== null){
            var playlist = JSON.parse(data).result;
            var songs = playlist.tracks;
            var pEle = $("#songs");
            for (var i=0; i<songs.length; i++){
                var song = songs[i];
                var trEle = $("<tr />");
                var indexEle = $("<td />");
                indexEle.text(i+1);
                var titleEle = $("<td />");
                titleEle.text(song.name);
                var artistEle = $("<td />");
                var artists = song.artists;
                var artistName = '';
                for (var j=0; j< artists.length; j++){
                    if (j>0) artistName += ', ';
                    artistName += artists[j].name + ' ';
                }
                artistEle.text(artistName);
                artistEle.attr("artistId", artists[0].id);

                var albumEle = $("<td />");
                albumEle.text(song.album.name);
                albumEle.attr("albumId", song.album.id);

                var durationEle = $("<td />");
                var duration = song.duration;
                var m = parseInt(duration / 60000);
                var s = parseInt(parseInt(duration % 60000)/1000);
                durationEle.text(m.toString() + ':' + s);

                trEle.append(indexEle);
                trEle.append(titleEle);
                trEle.append(artistEle);
                trEle.append(albumEle);
                trEle.append(durationEle);

                pEle.append(trEle);
                console.log("add a songs");
            }
        }
    }
};
