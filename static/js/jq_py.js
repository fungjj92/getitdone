/**
 * Created by jenny on 5/19/15.
 */

$(document).ready(function(){

    /* When a new to-do is entered, prevent server refresh,
    grab input data and add to lists with functionality */
    $("form").submit(function(event) {
        event.preventDefault();

        var task = $('#newtask').val();
        var date = $('#datepicker').val();
        var createdTask = createTask(task, date);

    }
}

function createTask(task, date){
    $.post(
            //todo here
    )
    //markup new task for loading to page
    var buttons = '<li draggable="true"><span class="handle">&nbsp; : : </span><button>&times;</button> ';
    if (date !== ""){
        var newTask = $(buttons + '<strong>' + date + '</strong> ' + task + '</li>');
        addTask(newTask);
    } else{
        var newTask = $(buttons + task + '</li>');
        addTask(newTask);
    }

}






        //Add task deletion function to button
        $("button", newTask).on("click", function(){
            $(this.parentNode).remove();
        });

        //allow for click activated movement of tasks between lists
        $(newTask).click(function(){
            if ($(this).parent().hasClass("tasklist")) {
                $(".completedlist").prepend(this);
            } else if ($(this).parent().hasClass("completedlist")){
                $(".tasklist").prepend(this);
            }
        });

        //call sort functionality on task lines
        $('.sortable').sortable({
            handle: '.handle'
        });

        //reset input areas to default state
        $("#addtasks")[0].reset();
    });


    //datepicker functionality
    $(function() {
        $( "#datepicker" ).datepicker();
    });

    function addTask(newTask){
        var container = $(".tasklist");
        container.prepend(newTask);
    }

})