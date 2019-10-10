$(document).ready(function() {
        fields = 0;
        $(".day_button").click(function(e) {
            day = $(this).attr('id')
            day = day.split("_")
            day = day[day.length - 1]
            fields++;
            $("#fields_" + day + "_0").clone().appendTo("#times_" + day).attr("id", "fields_" + day + '_' + fields).attr("name", "fields_" + day + '_' + fields);
        })
});