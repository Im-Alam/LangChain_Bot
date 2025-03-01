css = """
<link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
<style>
    .chat-message{
        display: flex;
        margin: 1rem 0rem;
    }   

    .chat-message .avatar{
        width: 50px;
    }

    
    .material-icons{
        font-size:3px;
    }

    .chat-message .message{
        width: 85%;
    }

    .chat-message.user .message{
        background: #373737;
        border-radius: 14px;  
        padding: 10px;
    }


</style>
"""

bot_template = """
<div class="chat-message bot">
    <div class="avatar">
        <i class="material-icons" style="font-size: 35px; color: #ffffff;">smart_toy</i>
    </div>
    <div class="message">{{msg}}</div>
</div>
"""



user_template = """
<div class="chat-message user">
    <div class="avatar">
        <i class="material-icons" style="font-size:35px; color:#ffffff;">account_circle</i>
    </div>
    <div class="message">{{msg}}</div>
</div>
"""