<h1>:wave: Hey there!</h1>
<p>I am Ivo, computational chemist :test_tube: and retro computer enthousiast :space_invader: from the Netherlands <img src="https://hatscripts.github.io/circle-flags/flags/nl.svg" width="16">.

<h2>Things, I like to work with</h2>
<p>
{%- for img in language_icons %}
<img src="{{ img }}" />
{%- endfor %}
</p>

<img src="https://github-readme-stats.vercel.app/api/top-langs/?username=ifilot&hide_progress=true" />
<img src="https://github-readme-stats.vercel.app/api?username=ifilot&show_icons=true" />

<h2>Computational chemistry projects</h2>
<table>
  <thead align="center">
    <tr border: none;>
      <td><b>Projects</b></td>
      <td><b>Languages</b></td>
      <td><b>Stars</b></td>
      <td><b>Issues</b></td>
      <td><b>Forks</b></td>
    </tr>
  </thead>
  <tbody>
  {%- for repo in ccp_repositories %}
    <tr>
      <td width="50%"><img src="https://github.com/primer/octicons/blob/main/icons/repo-16.svg" width="16" /> 
          <a href="{{ repo.link }}">{{ repo.repo }}</a><br>
          <small style="color: gray;"><i>{{ repo.description }}</i></small>
      </td>
      <td>
        {%- for lang in repo.languages -%}
            {{ lang.language }}{% if not loop.last %}, {% endif %}
        {%- endfor -%}
      </td>
      <td align="center"><img src="https://github.com/primer/octicons/blob/main/icons/star-16.svg" width="16" /> {{ repo.stars }}
      </td>
      <td align="center"><img src="https://github.com/primer/octicons/blob/main/icons/issue-opened-16.svg" width="16" /> {{ repo.issues }}
      </td>
      <td align="center"><img src="https://github.com/primer/octicons/blob/main/icons/repo-forked-16.svg" width="16" /> {{ repo.forks }}
      </td>
    </tr>
  {%- endfor %}
  </tbody>
</table>

<h2>Retro computing</h2>

<h3>Philips P2000T and P2000C</h3>
<table>
  <thead align="center">
    <tr border: none;>
      <td><b>Projects</b></td>
      <td><b>Languages</b></td>
      <td><b>Stars</b></td>
      <td><b>Issues</b></td>
      <td><b>Forks</b></td>
    </tr>
  </thead>
  <tbody>
  {%- for repo in p2k_repositories %}
    <tr>
      <td width="50%"><img src="https://github.com/primer/octicons/blob/main/icons/repo-16.svg" width="16" /> 
          <a href="{{ repo.link }}">{{ repo.repo }}</a><br>
          <small style="color: gray;"><i>{{ repo.description }}</i></small>
      </td>
      <td>
        {%- for lang in repo.languages -%}
            {{ lang.language }}{% if not loop.last %}, {% endif %}
        {%- endfor -%}
      </td>
      <td align="center"><img src="https://github.com/primer/octicons/blob/main/icons/star-16.svg" width="16" /> {{ repo.stars }}
      </td>
      <td align="center"><img src="https://github.com/primer/octicons/blob/main/icons/issue-opened-16.svg" width="16" /> {{ repo.issues }}
      </td>
      <td align="center"><img src="https://github.com/primer/octicons/blob/main/icons/repo-forked-16.svg" width="16" /> {{ repo.forks }}
      </td>
    </tr>
  {%- endfor %}
  </tbody>
</table>

<h2>Open source hardware/software</h2>
<table>
  <thead align="center">
    <tr border: none;>
      <td><b>Projects</b></td>
      <td><b>Languages</b></td>
      <td><b>Stars</b></td>
      <td><b>Issues</b></td>
      <td><b>Forks</b></td>
    </tr>
  </thead>
  <tbody>
  {%- for repo in oshw_repositories %}
    <tr>
      <td width="50%"><img src="https://github.com/primer/octicons/blob/main/icons/repo-16.svg" width="16" /> 
          <a href="{{ repo.link }}">{{ repo.repo }}</a><br>
          <small style="color: gray;"><i>{{ repo.description }}</i></small>
      </td>
      <td>
        {%- for lang in repo.languages -%}
            {{ lang.language }}{% if not loop.last %}, {% endif %}
        {%- endfor -%}
      </td>
      <td align="center"><img src="https://github.com/primer/octicons/blob/main/icons/star-16.svg" width="16" /> {{ repo.stars }}
      </td>
      <td align="center"><img src="https://github.com/primer/octicons/blob/main/icons/issue-opened-16.svg" width="16" /> {{ repo.issues }}
      </td>
      <td align="center"><img src="https://github.com/primer/octicons/blob/main/icons/repo-forked-16.svg" width="16" /> {{ repo.forks }}
      </td>
    </tr>
  {%- endfor %}
  </tbody>
</table>

<h2>Open education</h2>
<table>
  <thead align="center">
    <tr border: none;>
      <td><b>Projects</b></td>
      <td><b>Languages</b></td>
      <td><b>Stars</b></td>
      <td><b>Issues</b></td>
      <td><b>Forks</b></td>
    </tr>
  </thead>
  <tbody>
  {%- for repo in osed_repositories %}
    <tr>
      <td width="50%"><img src="https://github.com/primer/octicons/blob/main/icons/repo-16.svg" width="16" /> 
          <a href="{{ repo.link }}">{{ repo.repo }}</a><br>
          <small style="color: gray;"><i>{{ repo.description }}</i></small>
      </td>
      <td>
        {%- for lang in repo.languages -%}
            {{ lang.language }}{% if not loop.last %}, {% endif %}
        {%- endfor -%}
      </td>
      <td align="center"><img src="https://github.com/primer/octicons/blob/main/icons/star-16.svg" width="16" /> {{ repo.stars }}
      </td>
      <td align="center"><img src="https://github.com/primer/octicons/blob/main/icons/issue-opened-16.svg" width="16" /> {{ repo.issues }}
      </td>
      <td align="center"><img src="https://github.com/primer/octicons/blob/main/icons/repo-forked-16.svg" width="16" /> {{ repo.forks }}
      </td>
    </tr>
  {%- endfor %}
  </tbody>
</table>