% include('layout.tpl')
<h2>Videoaulas</h2>

% if aluno:
    <p>Aluno: {{aluno.name}} (Matrícula: {{aluno.matricula}})</p>
% end

<ul>
% for v in videos:
    <li>
        <strong>{{v.titulo}}</strong> - {{v.disciplina or 'Geral'}}
        <br>
        <a href="{{v.url}}" target="_blank">Assistir</a>
        % if aluno and (v.id in (aluno.videos_assistidos or [])):
            <em> — assistido</em>
        % else:
            % if aluno:
                <form method="post" action="/videoaulas/watch/{{v.id}}">
                    <input type="hidden" name="aluno_id" value="{{aluno.id}}">
                    <button type="submit">Marcar como assistido</button>
                </form>
            % end
        % end
    </li>
% end
</ul>
