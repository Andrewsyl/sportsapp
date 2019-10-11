$(document).ready(function() {
//        fields = 0;
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

        var current_id = 0;
        $('.day_button').click(function(){
            day = $(this).attr('id')
            day = day.split("_")
            day = day[day.length - 1]
            nextElement($("#fields_"+day+"_0"),day);

        })

        function nextElement(element,day){
            var newElement = element.clone();
            var id = current_id+1;
            current_id = id;
            newElement.attr("id",(element.attr("id").split("_")[0] + "_" + day + "_" + current_id));
            newElement.attr("name",(element.attr("id").split("_")[0] + "_" + day + "_" + current_id));
            var field = $('select', newElement).attr("id");
            //field = field.slice(0,field.length - 1) + "_" + current_id

            $('select', newElement).attr("name", field);
            newElement.appendTo("#times_" + day);
        }

});