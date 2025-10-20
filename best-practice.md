# Best Practices for Subagent Usage

## English

When using subagents in OpenCode, it is highly recommended to call them **after** your message rather than before. OpenCode frequently encounters JSON parsing errors when a subagent is invoked before the main message content. 

**What NOT to do:**
```
@github-action, can you commit
```
*Risk: JSON parsing error*

**What TO do:**
```
Can you commit @github-action
```
*This method has consistently worked without issues*

This approach should be used until OpenCode resolves the parsing errors internally. By placing the subagent call at the end of your message, you significantly reduce the likelihood of encountering technical issues and ensure smoother workflow execution.

---

## Français

Lors de l'utilisation des subagents dans OpenCode, il est fortement recommandé de les appeler **après** votre message plutôt qu'avant. OpenCode rencontre fréquemment des erreurs d'analyse JSON lorsqu'un subagent est invoqué avant le contenu principal du message.

**À NE PAS faire :**
```
@github-action, peux-tu commit
```
*Risque : erreur d'analyse JSON*

**À faire :**
```
Peux-tu commit @github-action
```
*Cette méthode a toujours fonctionné sans problème*

Cette approche doit être utilisée tant qu'OpenCode ne résout pas les erreurs d'analyse en interne. En plaçant l'appel du subagent à la fin de votre message, vous réduisez considérablement la probabilité de rencontrer des problèmes techniques et assurez une exécution de workflow plus fluide.