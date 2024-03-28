namespace TodoListItem;

public class TodoItem //creates a public class that is a blueprint for creating objects. 
{
    public string? Title { get; set; } //creates a public property - data type is string? the ? allows it to hold data.
    public bool IsDone { get; set; } //getter retrieves data, allows private access to input outside the class, 
    //setters allows the settings of a value to the property, allowing the assignemtn of data to private inputs
}