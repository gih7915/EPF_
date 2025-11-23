% include('layout.tpl')
<h1>Videoaulas</h1>

% if aluno:
    <div class="aluno-info" style="background: #ecf0f1; padding: 15px; border-radius: 4px; margin-bottom: 20px;">
        <p><strong>Aluno:</strong> {{aluno.name}}</p>
        <p><strong>Matrícula:</strong> {{aluno.matricula}}</p>
        <p><strong>Curso:</strong> {{aluno.curso}}</p>
    </div>
% else:
    <p><em>Selecione um aluno para visualizar suas videoaulas.</em></p>
% end

<div class="videoaulas-list">
% for v in videos:
    <div class="video-item">
        <strong>{{v.titulo}}</strong>
        <span class="badge badge-info">{{v.disciplina or 'Geral'}}</span>
        % if v.duracao:
            <span class="item-meta" style="margin-left: 10px;">⏱ {{v.duracao}} min</span>
        % end
        <p>{{v.descricao or ''}}</p>
        <div class="item-actions">
            <a href="{{v.url}}" target="_blank" class="btn">Assistir Vídeo</a>
            % if aluno and (v.id in (aluno.videos_assistidos or [])):
                <span class="badge badge-success">✓ Assistido</span>
            % else:
                % if aluno:
                    <form method="post" action="/videoaulas/watch/{{v.id}}" style="display: inline;">
                        <input type="hidden" name="aluno_id" value="{{aluno.id}}">
                        <button type="submit" class="btn btn-success">Marcar como Assistido</button>
                    </form>
                % end
            % end
        </div>
    </div>
% end
</div>
