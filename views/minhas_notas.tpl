% rebase('layout', title='Notas', nav_dict=nav_dict if 'nav_dict' in locals() else {})

<div class="titulo">
    <h1>Minhas Notas</h1>
    <p>Verifique seu desempenho nas avaliações</p>
</div>

% if aluno:
    <div class="aluno-info" style="background: #ecf0f1; padding: 12px; border-radius:4px; margin-bottom:16px;">
        <p><strong>Aluno:</strong> {{aluno.name}} &nbsp; <strong>Matrícula:</strong> {{aluno.matricula}}</p>
    </div>

    <form method="get" action="/minhas_notas" style="margin-bottom:18px;">
        <input type="hidden" name="aluno_id" value="{{aluno.id}}">
        <label for="disciplina_codigo">Selecione a disciplina:</label>
        <select name="disciplina_codigo" id="disciplina_codigo" style="margin-left:8px;">
            <option value="" disabled selected>Selecione</option>
            % for d in (disciplinas_matriculadas or []):
                <option value="{{d.codigo}}" % if disciplina_selecionada and disciplina_selecionada.codigo == d.codigo: selected % end>{{d.codigo}} - {{d.nome}}</option>
            % end
        </select>
        <button class="btn" type="submit" style="margin-left:8px;">Ver Notas</button>
    </form>

    % if disciplina_selecionada:
        <h2 style="margin-top:6px;">Disciplina: {{disciplina_selecionada.nome}} ({{disciplina_selecionada.codigo}})</h2>
        % if media is not None:
            <p><strong>Média:</strong> {{"{:.2f}".format(media)}}</p>
        % end

        % if notas_entries:
            <table class="table" style="width:100%; border-collapse:collapse;">
                <thead>
                    <tr>
                        <th class="table-header">Avaliação / Tarefa</th>
                        <th class="table-header">Entrega</th>
                        <th class="table-header">Nota</th>
                        <th class="table-header">Feedback</th>
                    </tr>
                </thead>
                <tbody>
                % for e in notas_entries:
                    % t = e['tarefa']
                    % s = e['submissao']
                    <tr>
                        <td style="padding:8px; border-bottom:1px solid #f1f1f1;"><strong>{{t.titulo}}</strong></td>
                        <td style="padding:8px; border-bottom:1px solid #f1f1f1;">% if s: {{s.entregue_em or '-'}} % else: Não entregue % end</td>
                        <td style="padding:8px; border-bottom:1px solid #f1f1f1;">% if s and s.nota is not None: {{"{:.2f}".format(s.nota)}} % else: — % end</td>
                        <td style="padding:8px; border-bottom:1px solid #f1f1f1;">% if s and s.feedback: {{s.feedback}} % else: - % end</td>
                    </tr>
                % end
                </tbody>
            </table>
        % else:
            <p><em>Nenhuma avaliação registrada nesta disciplina ainda.</em></p>
        % end

    % else:
        <p><em>Selecione uma disciplina para visualizar suas notas.</em></p>
    % end

% else:
    <p><em>Aluno não informado. Acesse pelo seu dashboard.</em></p>
% end
