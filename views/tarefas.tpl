% rebase('layout', title='Tarefas', nav_dict=nav_dict if 'nav_dict' in locals() else {})
<h1>Tarefas</h1>

% if aluno:
    <div class="aluno-info" style="background: #ecf0f1; padding: 15px; border-radius: 4px; margin-bottom: 20px;">
        <p><strong>Aluno:</strong> {{aluno.name}}</p>
        <p><strong>Matrícula:</strong> {{aluno.matricula}}</p>
        <p><strong>Curso:</strong> {{aluno.curso}}</p>
    </div>
% else:
    <p><em>Selecione um aluno para visualizar suas tarefas.</em></p>
% end

<div class="tarefas-list">
% for t in tarefas:
    <div class="tarefa-item">
        <strong>{{t.titulo}}</strong>
        <span class="badge badge-info">{{t.disciplina or 'Geral'}}</span>
        % if t.max_points:
            <span class="item-meta" style="margin-left: 10px;">Valor: {{t.max_points}} pontos</span>
        % end
        <p>{{t.descricao or ''}}</p>
        % if t.prazo:
            <p class="item-meta">📅 Prazo: <strong>{{t.prazo}}</strong></p>
        % end
        % if aluno:
            % if str(t.id) in (aluno.entregas or {}):
                <div class="badge badge-success">✓ Entregue</div>
                <button onclick="window.location.href='/tarefas/submit/{{t.id}}?aluno_id={{aluno.id}}'" class="btn" style="margin-top: 10px;">Reenviar Tarefa</button>
            % else:
                <button onclick="window.location.href='/tarefas/submit/{{t.id}}?aluno_id={{aluno.id}}'" class="btn" style="margin-top: 10px;">Entregar Tarefa</button>
            % end
        % end
    </div>
% end
</div>
