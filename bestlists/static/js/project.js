$('#editItemModal').on('show.bs.modal', function (event) {
    var button = $(event.relatedTarget);
    var itemUpdateUrl = button.data('itemUpdateUrl');
    var itemDescription = button.data('itemDescription');
    $(this).find('#id_description').val(itemDescription);
    $(this).find('form').attr('action', itemUpdateUrl);
}).on('shown.bs.modal', function () {
    $(this).find('#id_description').focus();
});

$('#editListModal').on('show.bs.modal', function (event) {
    var button = $(event.relatedTarget);
    // var todoListObj = button.data('todoList');
    var itemUpdateUrl = button.data('listUpdateUrl');
    $(this).find('form').attr('action', itemUpdateUrl);
}).on('shown.bs.modal', function () {
    $(this).find('#id_description').focus();
});