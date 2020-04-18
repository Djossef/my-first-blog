$(function() {
    setTimeout(function() {
        $('#parag1').fadeIn();
        setTimeout(function() {
            $('#parag2').fadeIn();
            setTimeout(function() {
                $('#morebtn').fadeToggle();
            }, 100);
        }, 500);
    }, 1000);


    $("#myDialog").dialog({
        autoOpen: false,
        buttons: {
            cancel: function() {
                $(this).dialog("close");
                window.location.replace("#about");
            }
        }
    });

    $("#open").click(function() {
        $("#myDialog").dialog("open");
    });

});