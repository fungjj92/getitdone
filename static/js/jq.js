/**
 * Created by jenny on 5/19/15.
 */

function addActions(task) {
    // ensure task is a jquery object
    task = $(task);

    //Add task deletion function to button
    task.find(".delete").click(function (event) {
        event.stopPropagation();
        //AJAX call to db
        var thistask = $(this.parentNode);
        $.post(
            '/list/delete',
            {'id': thistask.attr('data-task-id')}
        )
            .done(function(data){
                //remove fxn
                thistask.remove();
            })
            .fail(function () {
                console.log("Unable to delete task")
            });
    });

    //Add task completion switch function to click
    task.click(function(){
        //make the found taskrow a jquery object
        var thistask = $(this);

        //AJAX call to db
        $.post(
            '/list/completed',
            {'id': thistask.attr('data-task-id')}
        )
            .done(function(data){
                //change completion status
                if ($(thistask).parent().hasClass("tasklist")) {
                    $(".completedlist").prepend(thistask);
                } else if ($(thistask).parent().hasClass("completedlist")){
                    $(".tasklist").prepend(thistask);
                }
            })
            .fail(function(){
               console.log("Unable to switch completion status")
            });
    })

    //add sort functionality to handles
    $('.sortable').sortable({
        handle: '.handle'
    });

}
//factored out function live adds new task to screen
function displayTask(newTask) {
    var container = $(".tasklist");
    container.prepend(newTask);
}

function createTask(taskText, dueDate){
    //AJAX call to db
    $.post(
        '/list/new',
        {'task': taskText, 'duedate': dueDate }
    )
        .done(function(data) {
            var buttons = '<li draggable="true" data-task-id="' + data.id + '"class="taskText"><span class="handle">&nbsp; : : </span><button class="delete">&times;</button>';
            if (dueDate !== '' && dueDate !== null){
                var newTask = $(buttons + '<strong>' + dueDate + '</strong> ' + taskText + '</li>');
            } else{
                var newTask = $(buttons + taskText + '</li>');
            }
            addActions(newTask);
            displayTask(newTask);
        })
        .fail(function(){
            console.log("Unable to create task")
        });
}

$(document).ready(function(){
    //Upon page load, all tasks in DB render by code in list.html
    //
    $(".tasklist li, .completedlist li").each(function(idx, task){
        addActions(task);
    });

    //datepicker functionality
    $(function() {
        $( "#datepicker" ).datepicker();
    });

    /* When a new to-do is entered, prevent server refresh, grab input
    data and add to lists with DOM interactivity/functionality */
    $("#addtasks").submit(function(event){
        //stop page submission
        event.preventDefault();

        //new task creation
        var taskText = $('#newtask').val();
        var dueDate = $('#datepicker').val();
        createTask(taskText, dueDate);

        //reset input areas to default state
        $("#addtasks")[0].reset();
    });
})