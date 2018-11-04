function select_input_mode(x) {
    var input_mode = x.value;
    if(input_mode==0)
    {
        $("#input_search").show();
        $("#text_input").show();
        $("#file_input").hide();
        $("#input_submit").show();
        $("#hdn_input_mode").val(input_mode);
    }
    else
    {
        $("#input_search").show();
        $("#text_input").hide();
        $("#file_input").show();
        $("#input_submit").show();
        $("#hdn_input_mode").val(input_mode);
    }
}

function submit_input()
{
    $("#home_form").submit();
}

function find_search_result(x)
{
    var input_value = x.value;
    try
    {

        if(input_value != undefined && input_value != "" && input_value != null) {

            //    Ajax Function to call for api search and result return
            $.ajax({
                async: false,
                type: "POST",
                url: "/search",
                data: {"word": input_value},
                contentType: "application/json; charset=utf-8",
                dataType: "json",
                success: function (response) {
                    // console.log("response from api =" + response);
                    var word_list = JSON.parse(response)

                    $("#search_box").autocomplete({
                        source: word_list
                    });
                }
            });

        }
        else
        {
            // console.log("No value in search box: Search Value =" + input_value);
        }
    }
    catch(error)
    {
        // console.log("error was="+error);

    }

}