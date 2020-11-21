function updateBoard(board){
	for (var i in board){
        for(var j in board){
            if (board[i][j] == "X"){
                board[i][j] = '<h3>X</h3>';
            }
            else if (board[i][j] == "O"){
                board[i][j] = '<h3>O</h3>';
            }
            else{
                board[i][j] = "<h3></h3>";
            }
        }
	}

	$("#00").html(board[0][0]);
	$("#01").html(board[0][1]);
	$("#02").html(board[0][2]);

	$("#10").html(board[1][0]);
	$("#11").html(board[1][1]);
	$("#12").html(board[1][2]);

	$("#20").html(board[2][0]);
	$("#21").html(board[2][1]);
	$("#22").html(board[2][2]);
}



$(document).ready(function(){
    $.get("/",'index.html')
    $.get("/getBoard", {}, function(response){
        var data = JSON.parse(response);
        updateBoard(data);
    });
    $.get("/init",{},function(response){
        var data = JSON.parse(response);
        updateBoard(data);
    });
    $.get("/status",{},function(response){
        var data = JSON.parse(response);
        var message = data["status"];
        $("#status").html(message);
    });
    $.get("/game_status",{},function(response){
        var data = JSON.parse(response);
        var message = data["game_status"];
        $("#game_status").html(message);
    });
    $('#00').click(function(){
        var location = {row: 0,col: 0}
        $.ajax({
            url: '/click',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify(location),
            dataType: 'text',
            success: function(result){
                $.get("/game_status",function(response){
                    var data = JSON.parse(response);
                    var message = data["result"];
                    $("#game_status").html(message);
                });
                $.get("/status",{},function(response){
                    var data = JSON.parse(response);
                    var message = data["result"];
                    $("#status").html(message);
                });
                var data = JSON.parse(result);
                updateBoard(data);
            },
            error: function(err){
                alert(location)
            }
        })
        return false
    });
    $('#01').click(function(){
        var location = {"row":0,"col":1};
        $.ajax({
            url: '/click',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify(location),
            dataType: 'text',
            success: function(result){
                $.get("/game_status",function(response){
                    var data = JSON.parse(response);
                    var message = data["result"];
                    $("#game_status").html(message);
                });
                $.get("/status",{},function(response){
                    var data = JSON.parse(response);
                    var message = data["result"];
                    $("#status").html(message);
                });
                var data = JSON.parse(result);
                updateBoard(data);
            },
            error: function(err){
                alert(location)
            }
        })
        return false
    });
    $('#02').click(function(){
        var location = {"row":0,"col":2};
        $.ajax({
            url: '/click',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify(location),
            dataType: 'text',
            success: function(result){
                $.get("/game_status",function(response){
                    var data = JSON.parse(response);
                    var message = data["result"];
                    $("#game_status").html(message);
                });
                $.get("/status",{},function(response){
                    var data = JSON.parse(response);
                    var message = data["result"];
                    $("#status").html(message);
                });
                var data = JSON.parse(result);
                updateBoard(data);
            },
            error: function(err){
                alert(location)
            }
        })
        return false
    });
    $('#10').click(function(){
        var location = {"row":1,"col":0};
        $.ajax({
            url: '/click',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify(location),
            dataType: 'text',
            success: function(result){
                $.get("/game_status",function(response){
                    var data = JSON.parse(response);
                    var message = data["result"];
                    $("#game_status").html(message);
                });
                $.get("/status",{},function(response){
                    var data = JSON.parse(response);
                    var message = data["result"];
                    $("#status").html(message);
                });
                var data = JSON.parse(result);
                updateBoard(data);
            },
            error: function(err){
                alert(location)
            }
        })
        return false
    });
    $('#11').click(function(){
        var location = {"row":1,"col":1};
        $.ajax({
            url: '/click',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify(location),
            dataType: 'text',
            success: function(result){
                $.get("/game_status",function(response){
                    var data = JSON.parse(response);
                    var message = data["result"];
                    $("#game_status").html(message);
                });
                $.get("/status",{},function(response){
                    var data = JSON.parse(response);
                    var message = data["result"];
                    $("#status").html(message);
                });
                var data = JSON.parse(result);
                updateBoard(data);
            },
            error: function(err){
                alert(location)
            }
        })
        return false
    });
    $('#12').click(function(){
        var location = {"row":1,"col":2};
        $.ajax({
            url: '/click',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify(location),
            dataType: 'text',
            success: function(result){
                $.get("/game_status",function(response){
                    var data = JSON.parse(response);
                    var message = data["result"];
                    $("#game_status").html(message);
                });
                $.get("/status",{},function(response){
                    var data = JSON.parse(response);
                    var message = data["result"];
                    $("#status").html(message);
                });
                var data = JSON.parse(result);
                updateBoard(data);
            },
            error: function(err){
                alert(location)
            }
        })
        return false
    });
    $('#20').click(function(){
        var location = {"row":2,"col":0};
        $.ajax({
            url: '/click',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify(location),
            dataType: 'text',
            success: function(result){
                $.get("/game_status",function(response){
                    var data = JSON.parse(response);
                    var message = data["result"];
                    $("#game_status").html(message);
                });
                $.get("/status",{},function(response){
                    var data = JSON.parse(response);
                    var message = data["result"];
                    $("#status").html(message);
                });
                var data = JSON.parse(result);
                updateBoard(data);
            },
            error: function(err){
                alert(location)
            }
        })
        return false
    });
    $('#21').click(function(){
        var location = {"row":2,"col":1};
        $.ajax({
            url: '/click',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify(location),
            dataType: 'text',
            success: function(result){
                $.get("/game_status",function(response){
                    var data = JSON.parse(response);
                    var message = data["result"];
                    $("#game_status").html(message);
                });
                $.get("/status",{},function(response){
                    var data = JSON.parse(response);
                    var message = data["result"];
                    $("#status").html(message);
                });
                var data = JSON.parse(result);
                updateBoard(data);
            },
            error: function(err){
                alert(location)
            }
        })
        return false
    });
    $('#22').click(function(){
        var location = {"row":2,"col":2};
        $.ajax({
            url: '/click',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify(location),
            dataType: 'text',
            success: function(result){
                $.get("/game_status",function(response){
                    var data = JSON.parse(response);
                    var message = data["result"];
                    $("#game_status").html(message);
                });
                $.get("/status",{},function(response){
                    var data = JSON.parse(response);
                    var message = data["result"];
                    $("#status").html(message);
                });
                var data = JSON.parse(result);
                updateBoard(data);
            },
            error: function(err){
                alert(location)
            }
        })
        return false
    });
});
