$(document).ready(function () {
   $.getJSON("text.json", function(data){
       var paste_data = ''
       $.each(data, function(key, value){
           paste_data += '<tr>';
           paste_data += '<td>'+value.text+'</td>';
           paste_data += '<td>'+value.key+'</td>';
           paste_data += '</tr>';
       });
       $('#paste_table').append(paste_data);
   });
});