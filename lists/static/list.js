window.Superlists = {};
window.Superlists.initialize = function(){
    $('input[name="text"]').on("keypress", function(){
        console.log("In here")
        $('.has-error').hide()
    });
};
