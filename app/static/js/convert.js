$(document).ready(function(){
    $('#clear').click(function() {
        $('#template').val('');
        $('#render').val('');
        $('#values').val('');
        $('#render').html('');
    });

    $('#convert').click(function() {
        var show_whitespaces = $('input[name="show_whitespaces"]').prop('checked');
        var dummy_values = $('input[name="dummy_values"]').prop('checked');
        var trim_blocks = $('input[name="trim_blocks"').prop('checked');
        var lstrip_blocks = $('input[name="lstrip_blocks"').prop('checked');
        var input_type = $('input[name="input_type"]:checked').val();


        // Push the input to the Jinja2 api (Python)
        $.ajax({
            type: 'POST',
            url: '/api/v1/render',
            data: JSON.stringify({
                "template": $('#template').val(),
                "values": $('#values').val(),
                "input_type": input_type,
                "show_whitespaces": show_whitespaces,
                "dummy_values": dummy_values,
                "trim_blocks": trim_blocks,
                "lstrip_blocks": lstrip_blocks
            }),
            contentType:"application/json"}).done(function(response) {
            // Grey out the white spaces chars if any
            response = response.replace(/•/g, '<span class="whitespace">•</span>');

            // Display the answer
            $('#render').html(response);
        });
    });
});
