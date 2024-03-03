$(document).ready(function () {
  let Amenitieschecked = {};
  $(document).on('change', "input[type='checkbox']", function () {
    if (this.checked) {
      Amenitieschecked[$(this).data('id')] = $(this).data('name');
    } else {
      delete Amenitieschecked[$(this).data('id')];
    }
    let lst = Object.values(Amenitieschecked);
    if (lst.length > 0) {
      $('div.amenities > h4').text(Object.values(Amenitieschecked).join(', '));
    } else {
      $('div.amenities > h4').html('&nbsp;');
    }
  });
});