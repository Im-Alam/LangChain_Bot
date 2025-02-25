css = """
<link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
<style>
    .chat-message .avatar{
        width: 15%;
    }

    
    
    .material-icons{
        font-size:3px;
    }

    .chat-message .message{
        width: 75%;
        padding: 0 1.5rem;
    }
</style>
"""

bot_template = """
<div class="chat-message bot">
    <div class="avatar">
        <i class="material-icons" style="font-size: 35px; color: #ffffff;">smart_toy</i>
    </div>
    <div class="message" style="padding-left: 0rem;">{{msg}}</div>
</div>
"""



user_template = """
<div class="chat-message user">
    <div class="avatar">
        <i class="material-icons" style="font-size:35px; color:#ffffff;">account_circle</i>
    </div>
    <div class="message" style="padding-left: 0rem;">{{msg}}</div>
</div>
"""