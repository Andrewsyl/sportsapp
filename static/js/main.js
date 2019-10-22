$(document).ready(function() {

        fields = 0;

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
            $('select', element).attr("name", $('select', element).attr("name"));
            var current_id = 0
            var newElement = element.clone();
            while ($("#fields" + "_" + day + "_" + current_id).length > 0){
                current_id++
            }
            //$('select', element).attr("name", $('select', element).attr("name") + "_" + current_id);
            newElement.attr("id",(element.attr("id").split("_")[0] + "_" + day + "_" + current_id)).attr('class','times_field');
            newElement.attr("name",(element.attr("id").split("_")[0] + "_" + day + "_" + current_id));
            var field = $('select', newElement).attr("name") + '_' + current_id;

            $('select', newElement).attr("name", field);
            newElement.appendTo("#times_" + day);
        }

});