$('#editItemModal').on('show.bs.modal', function (event) {
    var button = $(event.relatedTarget);
    var itemUpdateUrl = button.data('itemUpdateUrl');
    var itemDescription = button.data('itemDescription');
    var alwaysShow = button.data('itemInMaster');
    $(this).find('#id_list_item_edit-description').val(itemDescription);
    $(this).find('#id_list_item_edit-always-show').prop('checked', alwaysShow === "True");
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