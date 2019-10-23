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
            var current_id = 0
            var newElement = element.clone();
            while ($("#fields" + "_" + day + "_" + current_id).length > 0){
                current_id++
            }
            newElement.attr("id",(element.attr("id").split("_")[0] + "_" + day + "_" + current_id)).attr('class','times_field');
            newElement.removeAttr('name')
            var field_start = $('select', newElement.children().eq(0)).attr("name") + '_' + current_id;
            var field_end = $('select', newElement.children().eq(1)).attr("name") + '_' + current_id;

            $('select', newElement.children().eq(0)).attr("name", field_start);
            $('select', newElement.children().eq(1)).attr("name", field_end);
            newElement.appendTo("#times_" + day);
        }

});