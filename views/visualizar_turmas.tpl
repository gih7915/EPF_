% rebase('layout', title='Turmas', nav_dict=nav_dict)

<div class="titulo">
        <h1>Visualização de turmas</h1>
        <p>Verifique e inscreva-se como docente</p>
</div>

<table class="table">
    <thead>
        <tr>
            <th>Código</th>
            <th>Nome</th>
            <th>Turma</th>
            <th>Período</th>
            <th>Docente</th>
            <th>Ação</th>
        </tr>
    </thead>
    <tbody>
    % for d in disciplinas:
        <tr>
            <td>{{d.codigo}}</td>
            <td>{{d.nome}}</td>
            <td>{{d.turma}}</td>
            <td>{{d.ano_periodo}}</td>
            <td>
                % if d.docente_id:
                    ID {{d.docente_id}}
                % else:
                    —
                % end
            </td>
            <td>
                % if not d.docente_id:
                <form method="post" action="/visualizar_turmas" style="display:inline">
                    <input type="hidden" name="disciplina_id" value="{{d.id}}" />
                    <button type="submit">Inscrever-me</button>
                </form>
                % else:
                    Já possui docente
                % end
            </td>
        </tr>
    % end
    </tbody>
</table>