function select_input_mode(x) {
    var input_mode = x.value;
    if(input_mode==0)
    {
        $("#input_search").show();
        $("#text_input").show();
        $("#file_input").hide();
        $("#input_submit").show();
    }
    else
    {
        $("#input_search").show();
        $("#text_input").hide();
        $("#file_input").show();
        $("#input_submit").show();
    }
}

function submit_input()
{
    $("#home_form").submit();
}

