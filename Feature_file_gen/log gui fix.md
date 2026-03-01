            ## 🛠️ Correção: geração de statements "Given"

            Este documento descreve a correção aplicada no gerador de arquivos de feature (método `add_to_feature_file`) para que os statements "Given" usem a sentença do campo `context` que contém a palavra-chave do hobby selecionado, em vez de usar sempre a primeira sentença.

            ---

            ### 📌 Problema (resumo)

            O código original procurava a sentença que contivesse a *name keyword* (nome), mas o correto é procurar a sentença que contenha a *hobby keyword* (hobby) selecionada pelo usuário. Por isso, em muitos casos a frase certa não era escolhida e o resultado ficava menos relevante.

            ---

            ### 🔍 Antes (trecho original)

            ```python
            # Add Given statements
            new_lines = []
            for context in relevant_contexts:
                # Extract the most relevant part of the context
                # Look for sentences that contain the name keyword
                name_keyword = self.selected_name_keyword.get()
                sentences = context.split(';')

                for sentence in sentences:
                    sentence = sentence.strip()
                    if name_keyword.lower() in sentence.lower():
                        # Format as Given statement
                        given_statement = f"    Given {sentence}\n"
                        new_lines.append(given_statement)
                        break
                else:
                    # If no specific sentence found, use the whole context
                    given_statement = f"    Given {context}\n"
                    new_lines.append(given_statement)
            ```

            ---

            ### ✅ Depois (trecho corrigido)

            ```python
            # Add Given statements
            new_lines = []
            for context in relevant_contexts:
                # Extract the most relevant part of the context
                # Look for sentences that contain the hobby keyword
                hobby_keyword = self.selected_hobby_keyword.get()
                sentences = context.split(';')

                for sentence in sentences:
                    sentence = sentence.strip()
                    if hobby_keyword.lower() in sentence.lower():
                        # Format as Given statement
                        given_statement = f"    Given {sentence}\n"
                        new_lines.append(given_statement)
                        break
                else:
                    # If no specific sentence found, use the whole context
                    given_statement = f"    Given {context}\n"
                    new_lines.append(given_statement)
            ```

            ---

            ### ✨ O que foi alterado

            - 🔁 Substituição da variável de busca: `name_keyword` -> `hobby_keyword`.
            - 📝 Atualização do comentário explicativo para refletir a lógica correta.
            - 🧭 Comportamento: agora o código percorre as sentenças separadas por `;` e retorna a sentença que contém o hobby selecionado; caso nenhuma sentença contenha a keyword, usa-se o `context` inteiro como fallback.

            ---

            ### 🧪 Como validar

            1. Execute o gerador/GUI que utiliza `add_to_feature_file`.
            2. Selecione um hobby diferente e verifique o arquivo `.feature` gerado.
            3. Confirme que o `Given` agora contém a sentença que inclui o hobby escolhido (e não só a primeira sentença).

            Dica: testar com linhas de `context` que contenham múltiplas sentenças separadas por `;` e onde apenas uma contenha a palavra-chave do hobby.

            ---

            ### 📎 Notas adicionais

            - Esta correção é de baixo risco e não altera a assinatura do método, apenas a lógica interna.
            - Se houver variações no separador de sentenças (por exemplo, `.` em vez de `;`), considere melhorar o parser dividindo por múltiplos separadores ou usando uma tokenização mais robusta.

            Se quiser, aplico também uma pequena suíte de testes (unitários) para cobrir o caso feliz e um caso de fallback — diga se quer que eu crie os testes em `Feature_file_gen/tests`.

            ---

            ✍️ Atualizado por: correção automática (formato Markdown) — descrição e exemplos em PT-BR
