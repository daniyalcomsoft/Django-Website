
$("input").on("change", function() {
    this.setAttribute(
        "data-date",
        moment(this.value, "yy-MM-DD")
        .format( this.getAttribute("data-date-format") )
    )
}).trigger("change")