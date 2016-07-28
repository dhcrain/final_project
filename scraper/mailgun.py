{% extends "base.html" %}

{% block hero %}
<div class="home-hero">

</div>
{% endblock %}
{% block body %}
    <div class="row">
        <div class="small-6 large-centered columns">
            {% if user.is_authenticated %}
            <p>Welcome, {{ request.user }} You are logged in</p>
            {% else %}
            <form class="" action="{% url 'login' %}" method="post">
                {% csrf_token %}
                {{ login_form.as_p }}
                <input class="expanded button" type="submit" name="login" value="Login">
            </form>
            <br>
            <hr>
            <h2 class="text-center">OR</h2>
            <a class="expanded button success" href="{% url 'register_view' %}"><b>Create an Account</b></a>
            {% endif %}
        </div>
    </div>
{% endblock %}
