import { 
  exchangeNpssoForCode, 
  exchangeCodeForAccessToken, 
  getUserTitles
} from "psn-api";

async function testPsn() {
  const npsso = process.env.psn_api;
  if (!npsso) {
    console.error("Erro: A variável de ambiente 'psn_api' não está definida.");
    return;
  }
  
  try {
    const accessCode = await exchangeNpssoForCode(npsso);
    const authorization = await exchangeCodeForAccessToken(accessCode);
    const titles = await getUserTitles(authorization, "me", { limit: 2 });
    console.log(JSON.stringify(titles, null, 2));
  } catch (error) {
    console.error("Error connecting to PSN:", error.message);
  }
}

testPsn();
