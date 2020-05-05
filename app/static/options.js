
$(document).ready(function () {
   $.getJSON('/files/text.json', function(data){
       var paste_data = ''
       $.each(data, function(key, value){
           paste_data += '<tr>';
           paste_data += '<td>'+value.text+'</td>';
           paste_data += '<td>'+value.key+'</td>';
           paste_data += '</tr>';
       });
       console.log(paste_data)
       $('#paste_table').append(paste_data);
   });
});