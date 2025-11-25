% rebase('layout', title='Cadastro', nav_dict={})

<section class="form-section">
    <h1>✨ Criar Conta</h1>

    % if user_class == "Prof":
        <h3>👨‍🏫 Cadastro do Professor</h3>
    % elif user_class == "Aluno":
        <h3>📚 Cadastro do Aluno</h3>
    % else:
        <h3>Bem-vindo à plataforma!</h3>
    % end
    
    <form action="{{action}}" method="post" class="form-container">
        % if user_class:
            <div class="form-group">
                <label for="name">Nome:</label>
                <input type="text" id="name" name="name" required>
            </div>
            
            <div class="form-group">
                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required>
            </div>
            
            <div class="form-group">
                <label for="birthdate">Data de Nascimento:</label>
                <input type="date" id="birthdate" name="birthdate" required>
            </div>

            % if user_class == "Prof":
                <div class="form-group">
                    <label for="cargo">Cargo:</label>
                    <select id="cargo" name="cargo" required>
                        <option value="" disabled selected>Selecione um cargo</option>
                        <option value="Professor">Professor(a)</option>
                        <option value="Coordenador">Coordenador(a)</option>
                        <option value="Diretor">Diretor(a)</option>
                    </select>
                </div>
            % elif user_class == "Aluno":
                <div class="form-group">
                    <label for="curso">Curso:</label>
                    <select id="curso" name="curso" required>
                        <option value="" disabled selected>Selecione um curso</option>
                        % for i in cursos:
                            <option value="{{i}}">{{i}}</option>   
                        % end
                    </select>
                </div>
                <div class="form-group">
                    <label for="matricula">Matrícula:</label>
                    <input type="text" id="matricula" name="matricula" required>
                </div>
            % end

            <div class="form-group">
                <label for="senha">Senha:</label>
                <input type="password" id="senha" name="senha" required>
            </div>

            <div class="form-actions">
                <button type="button" onclick="window.location.href='/signup/wipe'" class="btn-cancel">
                        <i class="fas fa-trash-alt"></i> Voltar
                </button>
                <button type="submit" class="btn-submit">Salvar</button>
            </div>
        % end

        % if not user_class:
            <div class="form-group">
                <label for="tipo">Tipo de Usuário:</label>
                <select id="tipo" name="tipo" required>
                    <option value="" disabled selected>Selecione uma opção</option>
                    <option value="Prof">Professor</option>
                    <option value="Aluno">Aluno</option>
                </select>
            </div>
            <div class="form-actions">
                <button type="submit" class="btn-submit">Avançar</button>
            </div>
        % end

        <div class="form-actions">
            <button type="button" onclick="window.location.href='/login'" class="btn-cancel">Login</button>
        </div>
    </form>
</section>