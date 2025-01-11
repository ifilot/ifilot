<h1>:wave: Hey there!</h1>
<p>I am Ivo, computational chemist :test_tube: and retro computer enthousiast :space_invader: from the Netherlands <img src="https://hatscripts.github.io/circle-flags/flags/nl.svg" width="16">.

<h2>I like to program with</h2>
<p>
{%- for img in language_icons %}
<img src="{{ img }}" />
{%- endfor %}
</p>

<h2>Computational chemistry projects</h2>
<table>
  <thead align="center">
    <tr border: none;>
      <td><b>Projects</b></td>
      <td><b>Stars</b></td>
      <td><b>Issues</b></td>
      <td><b>Forks</b></td>
    </tr>
  </thead>
  <tbody>
  {%- for repo in ccp_repositories %}
    <tr>
      <td><a href="{{ repo.link }}">{{ repo.repo }}</a><br>
          <i>{{ repo.description }}</i>
      </td>
      <td>{{ repo.stars }}</td>
      <td>{{ repo.issues }}</td>
      <td>{{ repo.forks }}</td>
    </tr>
  {%- endfor %}
  </tbody>
</table>

<h2>Retro computing</h2>