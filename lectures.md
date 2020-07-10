---
layout: page
title: Lectures
permalink: /lectures/
---

Clicking the title of the lecture will open the slides in your browser. The icon <i class="fab fa-github"></i> links to the Github directory for the lecture, <i class="fab fa-r-project"></i> to the Rmarkdown document, and <i class="fas fa-video"></i> to the video recording. If video is not available, the icon will show as <i class="fas fa-video-slash"></i>. 

<!-- 
If possible, would like to have html slides stored locally rather than linking to GitHub
--> 

<ul id="archive">
{% for lectures in site.data.lectures %}
      <li class="archiveposturl">
        <span><a href="{{ site.url }}{{ site.baseurl }}/{{ lectures.dirname }}/{{ lectures.filename }}.html">{{ lectures.title }}</a></span><br>
<span class = "postlower">
<strong>tl;dr:</strong> {{ lectures.tldr }}</span>
<strong style="font-size:100%; font-family: 'Titillium Web', sans-serif; float:right; padding-right: .5em">
	<a href="https://github.com/{{ site.githubdir}}/tree/master/{{ lectures.dirname }}"><i class="fab fa-github"></i></a>&nbsp;&nbsp;
<a href="https://github.com/{{ site.githubdir}}/tree/master/{{ lectures.dirname }}/{{ lectures.filename}}.Rmd"><i class="fab fa-r-project"></i></a>&nbsp;&nbsp;
{% if lectures.recording == "" %}
<i class="fas fa-video-slash"></i>
{% else %}
<a href="{{lectures.recording}}"><i class="fas fa-video"></i></a>
{% endif %}

</strong> 
      </li>
{% endfor %}
</ul>
