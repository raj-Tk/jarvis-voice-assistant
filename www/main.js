$('.text').textillate({
    loop: true,
    sync: true,
    in: {
        effect: "animate__bounceIn"
    },
    out: {
        effect: "animate__bounceOut"
    }
});

$(document).ready(function () {

    // TEXT animation
    $('.text').textillate({
        loop: true,
        in: {
            effect: "bounceIn"
        },
        out: {
            effect: "bounceOut"
        }
    });

    // Siri wave
    var siriWave = new SiriWave({
        container: document.getElementById("siri-container"),
        width: 800,
        height: 200,
        style: "ios9",
        speed: 0.08,
        amplitude: 0.7,
        autostart: true,
    });

    // Siri message animation
    $('.siri-message').textillate({
        loop: true,
        in: {
            effect: "fadeInUp",
            sync: true,
        },
        out: {
            effect: "fadeOutUp",
             sync: true,
        }
    });

});