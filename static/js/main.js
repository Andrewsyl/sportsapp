$(document).ready(function() {
        fields = 0;
        $(".day_button").click(function(e) {
            day = $(this).attr('id')
            day = day.split("_")
            day = day[day.length - 1]
            $("#fields_" + day).clone().appendTo($("<div></div>").attr("id", "fields " + "_day_" + fields++).attr("name", "fields" + "_day_" + fields++).appendTo("#times_" + day));
        })
});