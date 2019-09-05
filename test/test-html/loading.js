const STYLE_FB = 0;

function addMask() {
    $("body").prepend('<div id="mask" class="mask"></div>')
    $("#mask").append('<div style="height:40%"></div>');
}

function addLoading(loadingStyleName) {
    loadingStyleName = arguments[0] || 0;
    if (STYLE_FB == loadingStyleName) {
        $("#mask").append('<div id="facebook"><div class="bar"></div><div class="bar"></div><div class="bar"></div></div>');
    }
}

function addLoadingMask() {
    addMask();
    addLoading(0);
}

function removeMask() {
    $("#mask").remove();
}