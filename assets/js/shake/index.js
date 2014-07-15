define(function(require) {
    require("jquery");
    require("bootstrap");

    var $rules;
    var $rulesOverlay;

    $(function() {
        $rules = $(".rules");
        $rulesOverlay = $(".rules-overlay");

        $rulesOverlay.click(function() {
            $rules.fadeOut();
            $rulesOverlay.fadeOut();
        });
        $rules.on('click', '.exit', function() {
            $rules.fadeOut();
            $rulesOverlay.fadeOut();
        });

        $(".button-bar .left").click(function() {
            $rules.fadeIn();
            $rulesOverlay.fadeIn();
        });
    });
});