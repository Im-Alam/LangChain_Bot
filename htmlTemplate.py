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

    .fixed-bottom {
        position: fixed;
        bottom: 0;
        left: 0;
        right: 0;
        background-color: white;
        padding: 10px;
        z-index: 1000;
        border-top: 1px solid #e1e4e8;
    }
    
    .chat-container {
        margin-bottom: 80px; /* Space for the input box */
        overflow-y: auto;
        height: calc(100vh - 120px); /* Adjust based on header and input box */
        padding: 10px;
    }

    /* Optional: Make the input box look nice */
    .stTextInput > div > input {
        width: 100%;
        padding: 10px;
        border: 1px solid #ddd;
        border-radius: 8px;

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