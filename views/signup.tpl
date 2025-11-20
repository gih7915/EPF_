% rebase('layout', title='Cadastro')

<section class="form-section">
    <h1>Cadastro</h1>

    % if user_class == "Prof":
        <h3>do Professor</h3>
    % end

    % if user_class == "Aluno":
        <h3>do Aluno</h3>
    % end
    
    <form action="{{action}}" method="post" class="form-container">
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
        % end

        <div class="form-group">
            <label for="senha">Senha:</label>
            <input type="password" id="senha" name="senha" required>
        </div>
        
        <div class="form-actions">
            <button type="submit" class="btn-submit">Salvar</button>
            <button type="button" onclick="window.location.href='/users'" class="btn-cancel">
                Voltar
            </button>
        </div>
    </form>
</section>