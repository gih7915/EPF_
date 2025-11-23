% include('layout.tpl')
<h2>Tarefas</h2>

% if aluno:
    <p>Aluno: {{aluno.name}} (Matrícula: {{aluno.matricula}})</p>
% end

<ul>
% for t in tarefas:
    <li>
        <strong>{{t.titulo}}</strong> - {{t.disciplina or 'Geral'}}
        <br>
        {{t.descricao or ''}}
        <br>
        Prazo: {{t.prazo or '—'}}
        % if aluno:
            <a href="/tarefas/submit/{{t.id}}?aluno_id={{aluno.id}}">Entregar tarefa</a>
        % end
    </li>
% end
</ul>
