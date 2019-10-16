$(document).ready(function() {

            fields = 0;
//        $(".day_button").click(function(e) {
//            day = $(this).attr('id')
//            day = day.split("_")
//            day = day[day.length - 1]
//            while ($("#fields_" + day + "_" + fields).length > 0){
//                fields++
//            }
//            var start_time = $("#selection").clone();
//            var end_time = $("#selection").clone();
//            $("#fields_" + day + "_0").clone().clone.find("Tuesday-start_time", "Tuesday-start_time_" + fields).appendTo("#times_" + day).attr("id", "fields_"+ day + '_' + fields).attr("name", "fields_" + day + '_' + fields);
//            fields = 0;
//
//        })

        $('.remove_button').click(function(){
            day = $(this).attr('id')
            day = day.split("_")
            day = day[day.length - 1]
            if ($('#times_' + day).children().length > 1) {
                $("#times_" + day + " div").last().remove();
             };
        })

        $('.add_button').click(function(){
            day = $(this).attr('id')
            day = day.split("_")
            day = day[day.length - 1]
            nextElement($("#fields_" + day + "_0"),day);
        })

        function nextElement(element,day){
            var current_id = 0
            var newElement = element.clone();
            while ($("#fields" + "_" + day + "_" + current_id).length > 0){
                current_id++
            }
            newElement.attr("id",(element.attr("id").split("_")[0] + "_" + day + "_" + current_id)).attr('class','times_field');
            newElement.attr("name",(element.attr("id").split("_")[0] + "_" + day + "_" + current_id));
            var field = $('select', newElement).attr("name");
            $('select', newElement).attr("name", $('select', newElement).attr("name") + "_" + current_id);
            newElement.appendTo("#times_" + day);
        }

});