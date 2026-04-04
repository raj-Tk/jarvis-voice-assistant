$(document).ready(function () {
    
$('.text').textillate({
    loop: true,
    sync: true,
    in:{
        effect: "animate_bounceIn",
    },

    out:{
        effect: "animate_bounceOut",
    },
});

});