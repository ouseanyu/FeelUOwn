var leftLayer = {

    need_captcha: false,
    captcha_id: null,

    login: function(){
        if (leftLayer.need_captcha === true) {
            var userCaptcha = $("#captcha").val();
            var result = python.confirm_captcha(captcha_id, userCaptcha);
            if (result !== true) {
                leftLayer.captcha_id = result;
                leftLayer.showCaptcha(leftLayer.captcha_id);
                return false;
            }
        }
        var username = $("#username").val();
        var password = $("#password").val();
        var data = python.login(username, password);
        data = JSON.parse(data);
        switch (data.code){
            case 200:
                leftLayer.loginSuccess(data);
                break;
            case 408:
                leftLayer.showLoginErrorMessage("Connection Timeout");
                break;
            case 415:
                leftLayer.showLoginErrorMessage("Captcha is needed");
                leftLayer.need_captcha = true;
                leftLayer.captcha_id = data.captchaId;
                leftLayer.showCaptcha(leftLayer.captcha_id);
                break;
            case 501:
                leftLayer.showLoginErrorMessage("Username not exist");
                break;
            case 502:
                leftLayer.showLoginErrorMessage("Password Error");
                break;
            case 509:
                leftLayer.showLoginErrorMessage("Please try again later, maybe 5 minutes");
                break;
            default:
                leftLayer.showLoginErrorMessage("Unknown Error");
                break;
        }
    },

    showCaptchar: function(captchaId){
        var url = python.captchar_url(captchaId);
        $(".captcha-container").show();
        $("#captcha").attr("src", url);
    },

    showLoginErrorMessage: function(text){
        $("#error").text(text);
    },
    
    setAvatar: function(url){
        var p_url = "url(" + url + ")";
        $("#avatar").css("background-image", p_url);
    },

    loginSuccess: function(data){
        console.log("Login Successfully");
        leftLayer.setAvatar(data.avatar);
        $(".login-container").hide();
    
        var p_data=null;
        p_data  = python.get_user_playlists();
        if (p_data !== null){
            p_data = JSON.parse(p_data);
            playlists = p_data.result;
            rightLayer.loadUserPlaylists(playlists);
        }
    }
};


$(function(){
    $("#login-btn").click(function(){
        leftLayer.login();
    });

    $("#password").bind("keydown", "return", function(){
        console.log("enter key");
        leftLayer.login();
    });
});
