$(document).ready(function() {
    // Handling the Todo Modal (Add vs Edit)
    $('#todoModal').on('show.bs.modal', function (event) {
        let button = $(event.relatedTarget);
        let todoId = button.data('id');

        let modal = $(this);
        let form = modal.find('#todo-form');
        let title = modal.find('.modal-title');

        if (todoId) {
            // EDIT MODE
            title.text('Update Task');

            let baseUrl = "{{ url_for('todo.update_todo', id='0') }}";
            let finalUrl = baseUrl.replace('0', todoId);
            form.attr('action', finalUrl);

            modal.find('#todo-id').val(todoId);
            modal.find('#title').val(button.data('title'));
            modal.find('#description').val(button.data('description'));
            modal.find('#priority').val(button.data('priority'));
            modal.find('#due_date').val(button.data('due_date'));
        } else {
            // ADD MODE
            title.text('Create New Task');
            form.attr('action', "{{ url_for('todo.create_todo') }}");

            if(form[0]) form[0].reset();
            modal.find('#todo-id').val('');
        }
    });

    // Form Submission UI Logic
    $('#todo-form').on('submit', function() {
        let btn = $(this).find('button[type="submit"]');
        btn.prop('disabled', true).html('<span class="spinner-border spinner-border-sm mr-2"></span>Saving...');
    });
});

$('#deleteModal').on('show.bs.modal', function (event) {
  console.log("Modal delete opening");
});
